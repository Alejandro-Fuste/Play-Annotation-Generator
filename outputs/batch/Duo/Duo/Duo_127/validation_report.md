# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_127`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_127/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 298 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
> - Action 'Action_PreSnap' range [0-298] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-212] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-252] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-259] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-266] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-208] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-298] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-298] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-274] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-277] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-280] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-296] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-271] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-298] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-289] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-281] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-298] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [181-186] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [196-199] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-194] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-199] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-234] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-298] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-273] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [190-196] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [207-241] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-261] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-268] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-196] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-251] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-213] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-237] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-244] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-220] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-223] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-298] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-252] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-258] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-296] for track '31' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.