# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_52`
- **Input XML**: `outputs/batch/Power/Power/Power_52/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [28-333] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-262] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-288] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-351] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-295] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-84] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-309] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-254] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-262] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-269] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-330] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-84] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-100] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-285] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-257] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-290] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-36] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-59] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-90] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-247] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-289] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-235] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-113] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [219-249] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-140] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-145] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-286] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-227] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-242] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-333] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-347] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-262] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-329] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-325] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-283] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-289] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-388] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-345] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-356] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [359-360] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [366-389] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-365] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-369] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-380] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-389] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [365-369] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-376] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-374] for track '31' has 2 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.