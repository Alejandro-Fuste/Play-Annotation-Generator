# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_110`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_110/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 67 |
| Player Tracks | 67 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 224 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Action 'Action_None' range [56-236] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-312] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-45] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-92] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-108] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-166] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-178] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-207] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-229] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-629] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-148] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [40-196] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [49-72] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-80] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-87] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-105] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-113] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-146] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-157] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-171] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-512] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-162] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-517] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [55-60] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [62-64] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-151] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-114] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-173] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-205] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-221] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-274] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-352] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-63] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-147] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [149-531] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-50] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-69] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-85] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-117] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-135] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-160] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-251] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-66] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-129] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-146] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-51] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-122] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-219] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [224-463] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-30] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-45] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-48] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-55] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-60] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-110] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-629] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-20] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-25] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-30] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-43] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-56] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-11] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-50] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-79] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-84] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-98] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-87] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-92] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-48] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-73] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-135] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-29] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-48] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-53] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-80] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [82-128] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-203] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-218] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-465] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-23] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-40] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-193] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-269] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-480] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [482-629] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-288] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-345] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-106] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-131] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-170] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-139] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-171] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-223] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-350] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-495] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-146] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-155] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-163] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-285] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-522] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [194-199] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-257] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-262] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-357] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [365-366] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-385] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [388-391] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [395-403] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-512] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-212] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-225] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-230] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-256] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-209] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-620] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [622-628] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-259] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-224] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-510] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-226] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-243] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-267] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [233-257] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-277] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-290] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-268] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-277] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [271-298] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-479] for track '41' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [279-298] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-310] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-489] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-307] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-316] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-400] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [403-406] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-528] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-531] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-504] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-361] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-371] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-376] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-387] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-392] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-419] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-422] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [429-430] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [436-448] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [452-463] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-473] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-476] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-488] for track '53' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [492-507] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-448] for track '54' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [450-452] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-387] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-458] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-430] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-526] for track '57' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [468-542] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [548-559] for track '58' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [562-566] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [568-570] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [496-497] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [502-504] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [515-519] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [596-597] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [542-549] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [551-561] for track '61' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [548-552] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [554-557] for track '62' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [549-550] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [555-559] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-567] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [589-590] for track '66' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.