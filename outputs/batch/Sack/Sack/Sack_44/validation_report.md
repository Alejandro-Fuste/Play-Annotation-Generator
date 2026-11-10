# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_44`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_44/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 46 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-100] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [80-87] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-108] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [98-103] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [110-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-43] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-88] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-96] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-49] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-40] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-48] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-75] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-88] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-44] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-83] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-61] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-81] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-120] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-117] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-115] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-101] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [106-107] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-120] for track '23' has 1 frames without a visible bounding box.
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