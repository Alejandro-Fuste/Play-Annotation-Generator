# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_63`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_63/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 52 |
| Player Tracks | 52 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 160 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (RG) duration 100 frames exceeds threshold 90 frames [start=61, end=160].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (LT) duration 100 frames exceeds threshold 90 frames [start=61, end=160].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 100 frames exceeds threshold 90 frames [start=61, end=160].
> - Action 'Action_None' range [38-128] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-112] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-139] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-401] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-345] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-395] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [64-129] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [132-160] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-184] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-258] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-278] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-392] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [404-405] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-413] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [38-134] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-347] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [350-369] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-360] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-227] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-357] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [363-365] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-370] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-135] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-155] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-182] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-419] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-250] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-387] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [389-397] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-413] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [38-219] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-238] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-135] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [138-144] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-148] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-397] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [404-405] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 76, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [76-76] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-213] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-247] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-419] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [38-167] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-370] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-209] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-326] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [328-413] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-81] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [136-137] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-387] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-395] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-404] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-85] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [93-139] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-397] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-405] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-96] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-192] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-231] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-238] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-250] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-275] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-419] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-217] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-225] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-173] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-250] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-312] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-216] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-374] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-384] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-397] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-401] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-414] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-416] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [258-260] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-282] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-271] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-282] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-419] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-296] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [298-300] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-317] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-343] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-315] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-301] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-330] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-346] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-370] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-381] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-330] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-335] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-343] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-357] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [384-387] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-401] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-405] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-417] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-398] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-415] for track '47' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [382-384] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-392] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-416] for track '50' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [414-416] for track '51' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.