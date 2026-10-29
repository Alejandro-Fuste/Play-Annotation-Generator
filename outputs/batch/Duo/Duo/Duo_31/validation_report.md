# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_31`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_31/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 54 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 268 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
> - Action 'Action_PreSnap' range [0-268] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-224] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-243] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-249] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-226] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-260] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-184] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-199] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-237] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-198] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-206] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-235] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-263] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-205] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-268] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-184] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-217] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-225] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-268] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-5] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-8] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-29] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-70] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-210] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-249] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-268] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-263] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-250] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-252] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-261] for track '27' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.