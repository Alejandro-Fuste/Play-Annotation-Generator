# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_220`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_220/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 49 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 442: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-66] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-90] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' for track '2' starts at frame 90, but the player has no visible bounding box on this frame.
> - Action 'Action_SackQuarterback' range [90-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-75] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-66] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-87] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-75] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-85] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-78] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-85] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-89] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-61] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-84] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-77] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-83] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-21] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-30] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-53] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-44] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-69] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [63-75] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [77-78] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-90] for track '23' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.