# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_286`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_286/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 161 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [81–93], lower_priority='Action_ZoneBlock' annotated_start=90, effective_Action_ZoneBlock_start=94.
> - Action 'Action_None' range [81-136] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-156] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-164] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [121-244] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [246-352] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [355-419] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-208] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-419] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [81-110] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-294] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [296-298] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-310] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-113] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-419] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-174] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-297] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-308] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-315] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-419] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-211] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-353] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [355-376] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [378-393] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [395-398] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-419] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [108-407] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-413] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-325] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-366] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [369-376] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [378-379] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-382] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-391] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-107] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-113] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-419] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-419] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-316] for track '15' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [328-343] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [345-375] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [378-379] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-392] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-398] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-403] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-417] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-266] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-274] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-290] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-304] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-311] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-317] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-323] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-332] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-342] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-346] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-357] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-367] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-405] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [90-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-120] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-282] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-419] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-98] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [116-141] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-419] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-350] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [366-369] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [374-375] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-386] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-394] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [398-415] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [90-113] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [142-406] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [408-414] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-133] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-137] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-148] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-159] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-272] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-339] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [342-378] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [380-395] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-185] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-209] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-217] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-229] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-248] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-260] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-261] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-268] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-303] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-292] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [315-317] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-350] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-372] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [374-376] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-342] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [348-352] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [354-362] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [366-368] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-389] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-394] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-398] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-404] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [410-413] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [415-419] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-371] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-404] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-408] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-413] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-419] for track '36' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.