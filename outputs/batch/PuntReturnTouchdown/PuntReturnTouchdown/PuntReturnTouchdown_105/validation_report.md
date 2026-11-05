# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_105`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_105/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 54 |
| Player Tracks | 54 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 214 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 211: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [105-256] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-265] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-444] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-253] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-265] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-623] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [33-407] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [412-515] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-92] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-116] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-150] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-168] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-385] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [388-500] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [503-524] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [529-537] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [539-584] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-102] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-109] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-128] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [131-273] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-171] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-278] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-97] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-103] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-141] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-81] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-128] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-142] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-150] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-118] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [120-127] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-471] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [473-581] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [586-594] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [598-601] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [606-615] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-268] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-96] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-122] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-129] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-180] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-186] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-195] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-220] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-325] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [330-399] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-402] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-54] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-313] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [315-326] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [334-417] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [33-88] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-97] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-407] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [412-440] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [442-446] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-546] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [548-574] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [592-616] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-15] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-62] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-15] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-56] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-112] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-71] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-118] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-112] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-116] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-205] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-450] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [454-470] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [485-629] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-124] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-473] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-478] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [487-488] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-257] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-277] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-215] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-377] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-581] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [584-607] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [611-620] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-166] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-372] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [376-601] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [606-629] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-162] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-163] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-238] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-267] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-277] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-303] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [245-260] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-298] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-244] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-509] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [511-597] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [269-521] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [526-547] for track '37' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [272-336] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-376] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-595] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-312] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [314-356] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [374-479] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [481-487] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-539] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [542-629] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-311] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-391] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-561] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [571-604] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [606-607] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-298] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-519] for track '42' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [523-524] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [527-629] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [313-608] for track '43' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [613-629] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-326] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-374] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [339-344] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-352] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-434] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-601] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [604-607] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [611-615] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [347-462] for track '46' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [464-629] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [429-467] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-476] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [484-567] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [572-580] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [583-586] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [456-459] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [468-629] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [510-525] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [528-532] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [534-536] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [538-547] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [550-555] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [557-559] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [562-575] for track '50' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [518-530] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [535-572] for track '51' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [575-582] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [588-591] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [599-601] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [609-613] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [626-627] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [565-575] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [577-595] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [573-574] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [588-620] for track '53' has 6 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.