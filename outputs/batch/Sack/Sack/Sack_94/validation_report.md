# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_94`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_94/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 41 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-96] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-117] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-97] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-84] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-37] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-41] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-15] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [73-75] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-78] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-81] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-120] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [103-108] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [111-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [117-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-88] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-120] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-104] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-106] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-120] for track '23' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.