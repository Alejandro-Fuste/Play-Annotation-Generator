# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_64`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_64/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 18 |
| Player Tracks | 18 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 32 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 130: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-82] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' for track '3' starts at frame 90, but the player has no visible bounding box on this frame.
> - Action 'Action_SackQuarterback' range [90-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-86] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-46] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-58] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-90] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-41] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-26] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-46] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-76] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-46] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-68] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-87] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-56] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-90] for track '17' has 2 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.