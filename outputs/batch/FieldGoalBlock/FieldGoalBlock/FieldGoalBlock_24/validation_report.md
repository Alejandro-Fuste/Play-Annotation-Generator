# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_24`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_24/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 69 |
| Player Tracks | 69 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 230 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 50: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - Row 50: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - Row 50: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 50: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 50: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_None' range [45-144] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-348] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-419] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-419] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-97] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-52] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-58] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-64] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-86] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-109] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-141] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-159] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-189] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-419] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-57] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-191] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-55] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-86] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-100] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-135] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-172] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-187] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-67] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-149] for track '8' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [151-167] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-239] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [1-347] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-419] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [45-57] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-113] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-142] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-196] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-216] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-271] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-276] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-348] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [353-370] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [377-388] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [392-393] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-121] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-174] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-213] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-282] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-310] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-327] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [330-337] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [345-355] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [358-372] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-384] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-389] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-84] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-23] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-19] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-108] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-182] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-20] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-144] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-167] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-258] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-27] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-36] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-52] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-144] for track '18' has 10 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-172] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-187] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-199] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-247] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-19] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-40] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-47] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-31] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-36] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-117] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-156] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-161] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-44] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-50] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-52] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-52] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-55] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-64] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-73] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-77] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-98] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-120] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-197] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-52] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-156] for track '27' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [75-82] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [84-87] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-181] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [94-107] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-121] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-133] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-197] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-211] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [213-220] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-101] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-125] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-108] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-120] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-138] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-160] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-205] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-128] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-184] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [118-178] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-184] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-138] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-144] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-182] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-207] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-200] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-376] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [379-384] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-396] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [398-406] for track '44' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [409-412] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-417] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-280] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-290] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-365] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-317] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-313] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-322] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [327-337] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-344] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-359] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-306] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-320] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-392] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [327-330] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-330] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-352] for track '55' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [335-336] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-357] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-350] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-355] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-374] for track '58' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [376-379] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-383] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-395] for track '58' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [400-401] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-409] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-414] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-353] for track '59' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [352-405] for track '60' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [407-416] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-357] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-358] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-366] for track '63' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [389-398] for track '63' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [374-376] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-396] for track '64' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [378-383] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-391] for track '66' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [407-409] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-409] for track '68' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.
> - Player track '56' has undefined position. Will map to Position_Unknown.
> - Player track '56' has undefined team_side. Will map to Team_Unknown.
> - Player track '57' has undefined position. Will map to Position_Unknown.
> - Player track '57' has undefined team_side. Will map to Team_Unknown.
> - Player track '58' has undefined position. Will map to Position_Unknown.
> - Player track '58' has undefined team_side. Will map to Team_Unknown.
> - Player track '59' has undefined position. Will map to Position_Unknown.
> - Player track '59' has undefined team_side. Will map to Team_Unknown.
> - Player track '60' has undefined position. Will map to Position_Unknown.
> - Player track '60' has undefined team_side. Will map to Team_Unknown.
> - Player track '61' has undefined position. Will map to Position_Unknown.
> - Player track '61' has undefined team_side. Will map to Team_Unknown.
> - Player track '62' has undefined position. Will map to Position_Unknown.
> - Player track '62' has undefined team_side. Will map to Team_Unknown.
> - Player track '63' has undefined position. Will map to Position_Unknown.
> - Player track '63' has undefined team_side. Will map to Team_Unknown.
> - Player track '64' has undefined position. Will map to Position_Unknown.
> - Player track '64' has undefined team_side. Will map to Team_Unknown.
> - Player track '65' has undefined position. Will map to Position_Unknown.
> - Player track '65' has undefined team_side. Will map to Team_Unknown.
> - Player track '66' has undefined position. Will map to Position_Unknown.
> - Player track '66' has undefined team_side. Will map to Team_Unknown.
> - Player track '67' has undefined position. Will map to Position_Unknown.
> - Player track '67' has undefined team_side. Will map to Team_Unknown.
> - Player track '68' has undefined position. Will map to Position_Unknown.
> - Player track '68' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.