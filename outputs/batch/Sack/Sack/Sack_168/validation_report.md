# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_168`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_168/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 52 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 338: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 338: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [66-67] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [70-72] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [76-77] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [86-89] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-46] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-71] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-90] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-46] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [77-81] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [84-85] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-66] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-46] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-90] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-48] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-67] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-48] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-77] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-81] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-19] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-42] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-73] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-90] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-89] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-90] for track '24' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.