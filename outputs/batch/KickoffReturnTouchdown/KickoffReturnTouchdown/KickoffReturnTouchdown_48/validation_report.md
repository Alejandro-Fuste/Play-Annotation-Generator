# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `KickoffReturnTouchdown_48`
- **Input XML**: `outputs/batch/KickoffReturnTouchdown/KickoffReturnTouchdown/KickoffReturnTouchdown_48/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/KickoffReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 60 |
| Player Tracks | 60 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 187 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 659 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
> - Segment 'Action_CatchKick' for track '29' has invalid range: start=238, end=197. Clamping end to start.
> - Segment 'Action_CrossGoalLine' for track '29' has invalid range: start=653, end=501. Clamping end to start.
> - Action 'Action_None' range [19-162] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-402] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-365] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-303] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-346] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [350-383] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [390-495] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-344] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-355] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-360] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-270] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-289] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-125] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-263] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-578] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [581-582] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-439] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [19-536] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-118] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-130] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-319] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-324] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-265] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-132] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-490] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [492-498] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-110] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-126] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-143] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-153] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-164] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-172] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-188] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-258] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-160] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-164] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-201] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-245] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-345] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-353] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-403] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-287] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-486] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-368] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-46] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-79] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-103] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-48] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-85] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-94] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-108] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-118] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-137] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-147] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-153] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-167] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-186] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [190-195] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-213] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-305] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [359-360] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-10] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-26] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-45] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-49] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-54] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-58] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-66] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-177] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-209] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-263] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-60] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-69] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-119] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-162] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-194] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-268] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-286] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-354] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [357-404] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-498] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-318] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-466] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [238-337] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [351-361] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [366-368] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [370-406] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [411-501] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-306] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-338] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [340-344] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-463] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-285] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-306] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-357] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-482] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-536] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [540-542] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [545-554] for track '33' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [303-355] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-659] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [311-376] for track '35' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [384-386] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-391] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-346] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-447] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-406] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [408-659] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-573] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [409-435] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-418] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-659] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-505] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [508-659] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [429-629] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [635-642] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [644-649] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [651-652] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [505-510] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [546-547] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [549-550] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [552-560] for track '46' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [566-567] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [555-558] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [558-569] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [561-565] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [567-568] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [596-649] for track '50' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [620-622] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [628-629] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [620-624] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [653-654] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [633-649] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [638-647] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [641-642] for track '59' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.