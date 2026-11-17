# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_150`
- **Input XML**: `outputs/batch/Power/Power/Power_150/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Action 'Action_PreSnap' range [14-425] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [435-446] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [455-457] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-433] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [315-347] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-401] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [409-415] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [420-479] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-432] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-342] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [315-320] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-443] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-449] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-374] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-401] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [439-448] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-336] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-327] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-333] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-370] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-479] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-208] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-315] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-321] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-333] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [366-367] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-384] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [389-390] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-396] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [438-441] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [337-468] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-398] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [401-414] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-426] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [405-455] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [406-463] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [418-435] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [441-450] for track '24' has 3 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.