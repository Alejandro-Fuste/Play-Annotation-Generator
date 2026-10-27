# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_194`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_194/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 19 |
| Player Tracks | 19 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 42 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '14' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_Handoff' for track '3' has invalid range: start=34, end=33. Clamping end to start.
> - Segment 'Action_BallCarry' for track '7' has invalid range: start=51, end=4. Clamping end to start.
> - Action 'Action_DownBlock' range [16-33] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '2' starts at frame 11, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [11-11] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-19] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-33] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-17] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-136] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-23] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-148] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-16] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-27] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-38] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-35] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-3] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-126] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-141] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-87] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-150] for track '18' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.