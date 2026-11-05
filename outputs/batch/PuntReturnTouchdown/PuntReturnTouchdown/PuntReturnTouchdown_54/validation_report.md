# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_54`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_54/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 45 |
| Ball Tracks | 1 |
| CSV events parsed | 16 |
| Action Segments inferred | 160 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [46-96] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-111] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-357] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-367] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-204] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-295] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-142] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-192] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-216] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-164] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-255] for track '4' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [258-286] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-295] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-307] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-101] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-129] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-389] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [46-115] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-214] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [232-285] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-371] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-389] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-66] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-122] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-151] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-336] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-389] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-159] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-190] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-272] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-60] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-104] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-284] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-296] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [299-335] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-88] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-100] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-92] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-283] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-289] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-62] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-131] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-166] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-389] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-83] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-107] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-151] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-304] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [46-64] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [80-81] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [85-93] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '16' starts at frame 94, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [94-214] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-249] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-64] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-155] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-257] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-92] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-114] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-133] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-148] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-228] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-96] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-110] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-115] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [203-257] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [260-301] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [305-328] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-44] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-53] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-143] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-219] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-342] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-34] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-28] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-44] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-54] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-59] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-79] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-164] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-183] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-203] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-279] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [282-306] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [310-313] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-351] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-359] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_CrossGoalLine' for track '26' starts at frame 360, but the player has no visible bounding box on this frame.
> - Action 'Action_CrossGoalLine' range [360-365] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-382] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-389] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-112] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-133] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-157] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-318] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [161-173] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-186] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-256] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-371] for track '31' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-250] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-294] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-389] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-289] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-323] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-274] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-303] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-280] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-285] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-340] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [342-363] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [371-372] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-380] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [337-389] for track '41' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.