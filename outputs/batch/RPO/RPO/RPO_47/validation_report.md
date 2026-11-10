# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_47`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_47/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 134 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_None' range [128-419] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [128-284] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-313] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-280] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-419] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-279] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-284] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-250] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-335] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [338-399] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [405-406] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-196] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-177] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-280] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-357] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-293] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-313] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-394] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [405-406] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-357] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [359-364] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-419] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-416] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [129-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [129-166] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '12' starts at frame 176, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [176-419] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-403] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-409] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-299] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-330] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-275] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-350] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [352-354] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-376] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-397] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-313] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [319-324] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-406] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-132] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-125] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-419] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [129-134] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [140-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [152-153] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-263] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-337] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-338] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-231] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-323] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-250] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-279] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-286] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-304] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-323] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [333-343] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [348-351] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-360] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-303] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-322] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-319] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-326] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-333] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [340-341] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-327] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-334] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [348-350] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-397] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-403] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-406] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-419] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-376] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [380-381] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-346] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-389] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [374-376] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-379] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-399] for track '41' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [404-405] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-397] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-419] for track '42' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.