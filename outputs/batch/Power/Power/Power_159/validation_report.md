# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_159`
- **Input XML**: `outputs/batch/Power/Power/Power_159/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_PreSnap' range [31-258] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-228] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-268] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-274] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-294] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-268] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-419] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-241] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-280] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-306] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-414] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-419] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-386] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-419] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-215] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-218] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-419] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-278] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-401] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-394] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-281] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-311] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-316] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-229] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [199-250] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-262] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-419] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-262] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-283] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-291] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-306] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-347] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-419] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-419] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-419] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-307] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-340] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-412] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-326] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-331] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-334] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-347] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [367-372] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-395] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [399-400] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [404-405] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [396-401] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [407-412] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [414-419] for track '35' has 2 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.