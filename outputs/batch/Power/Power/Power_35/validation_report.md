# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_35`
- **Input XML**: `outputs/batch/Power/Power/Power_35/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_PreSnap' range [6-397] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [399-400] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [402-419] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-419] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-330] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-393] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-364] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-282] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-350] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-361] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [363-364] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-335] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-83] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-257] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-247] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-22] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-36] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [247-256] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [267-284] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-302] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [311-312] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-325] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-393] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [396-417] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-288] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-303] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-246] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-279] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-419] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-304] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-396] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-353] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-357] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-364] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [366-372] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-398] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [401-402] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [407-416] for track '30' has 3 frames without a visible bounding box.
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