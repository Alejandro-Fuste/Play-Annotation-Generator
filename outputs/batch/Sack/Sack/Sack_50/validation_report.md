# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_50`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_50/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 21 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 27 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-140] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' for track '16' starts at frame 150, but the player has no visible bounding box on this frame.
> - Action 'Action_SackQuarterback' range [150-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-150] for track '20' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.