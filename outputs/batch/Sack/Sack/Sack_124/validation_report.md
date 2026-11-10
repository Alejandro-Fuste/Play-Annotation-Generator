# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_124`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_124/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 20 |
| Player Tracks | 20 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 38 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-137] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-180] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-180] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-158] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-171] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-148] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-113] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-160] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [83-97] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [105-113] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-79] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-119] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-162] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-153] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-172] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-180] for track '19' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.