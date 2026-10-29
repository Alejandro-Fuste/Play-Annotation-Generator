# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_30`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_30/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 29 |
| Ball Tracks | 1 |
| CSV events parsed | 14 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 268 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
> - Action 'Action_PreSnap' range [0-250] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-223] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-230] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-256] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-215] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-230] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-238] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-248] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-268] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-214] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-213] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-222] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-251] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-268] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-206] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-224] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-228] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-255] for track '10' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-230] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-267] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-183] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-189] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-230] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-254] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-88] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-66] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-184] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [185-196] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [198-240] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-255] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-80] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [185-189] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [204-205] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-157] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-268] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-268] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-230] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-199] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-214] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-223] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-220] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-234] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-268] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.