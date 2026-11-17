# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_241`
- **Input XML**: `outputs/batch/Power/Power/Power_241/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Action 'Action_PreSnap' range [10-551] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-499] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [505-507] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [521-526] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-379] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [381-543] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-569] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-25] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-45] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-499] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-376] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [418-472] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [478-482] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-378] for track '12' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [381-461] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-493] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [497-498] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [515-569] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-482] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [488-512] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-391] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-395] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [402-569] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-367] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-414] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [419-452] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [454-458] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [463-466] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [470-503] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [510-512] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-33] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-41] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-152] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-159] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-224] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-375] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [389-396] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-44] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-389] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [398-451] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [455-457] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [463-469] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [471-569] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-43] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-203] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-370] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-45] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-139] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-370] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [371-379] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-415] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-249] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-314] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [371-381] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-413] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-431] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [487-498] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [505-507] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-378] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [381-459] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [462-512] for track '23' has 7 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [517-522] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [525-526] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [533-569] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-429] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [442-443] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [466-569] for track '27' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.