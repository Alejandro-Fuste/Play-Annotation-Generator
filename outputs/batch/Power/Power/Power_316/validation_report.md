# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_316`
- **Input XML**: `outputs/batch/Power/Power/Power_316/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [18-246] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [190-194] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [198-209] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [216-238] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-166] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-175] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [190-199] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-255] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-258] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-144] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-223] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-288] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-320] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-234] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [190-220] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [239-258] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-252] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-23] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-35] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-46] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-184] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-208] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-217] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-271] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-228] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-216] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-228] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-253] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-238] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-189] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-260] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-199] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-203] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-221] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-255] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-285] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-226] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-231] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-260] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-286] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-299] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-309] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-315] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-322] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-264] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-293] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-329] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-286] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-295] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-283] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-320] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-307] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-319] for track '28' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.