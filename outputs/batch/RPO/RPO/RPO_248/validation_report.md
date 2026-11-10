# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_248`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_248/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 103 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [89-165] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-123] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-115] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [75-258] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [75-130] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-155] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-295] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-159] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-152] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-159] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-192] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [79-115] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [122-299] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [75-100] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [110-113] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-140] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-181] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-117] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-71] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-140] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-83] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-64] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-168] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [170-264] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-299] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-14] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-63] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-83] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-98] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-128] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-170] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-96] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-129] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-295] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-98] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-104] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-109] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-115] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-187] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-223] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-149] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-174] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-215] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-250] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-255] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-278] for track '36' has 1 frames without a visible bounding box.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.