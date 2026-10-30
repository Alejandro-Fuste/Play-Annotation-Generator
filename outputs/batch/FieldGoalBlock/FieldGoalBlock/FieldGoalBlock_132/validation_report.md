# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_132`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_132/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 176 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 266: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Action 'Action_KickBall' range [31-42] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-47] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-55] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-63] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-144] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-178] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-190] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [31-105] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' for track '2' starts at frame 30, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [30-30] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-36] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-89] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-147] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-87] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-164] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-81] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-101] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-113] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-131] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-180] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-246] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-282] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-389] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-416] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-100] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [102-104] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-212] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-250] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-265] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-273] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-286] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-306] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-315] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-8] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-157] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-173] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-191] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-53] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-163] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-173] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-23] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-41] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-47] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-60] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-7] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-30] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-88] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [90-96] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-231] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-265] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-341] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [346-410] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [415-419] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-422] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [425-436] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [442-443] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-194] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-449] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-22] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-30] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-55] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-63] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-87] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-110] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-213] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [215-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-13] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-28] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-38] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-105] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-143] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-75] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-25] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-28] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-105] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [32-81] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-41] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [42-57] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-113] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-160] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-172] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-82] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-157] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-128] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-187] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-87] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-103] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-173] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-106] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-148] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-113] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-142] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-195] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-211] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-282] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-337] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-182] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-135] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-204] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-223] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-168] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-175] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-208] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-209] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-217] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-276] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-377] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-423] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-312] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-438] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-290] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-328] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-287] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-351] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-384] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-449] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-294] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-298] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-309] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [311-314] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-345] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-395] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-444] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-319] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-336] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [339-342] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [345-379] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [383-407] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-414] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-436] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-354] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-357] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-436] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-443] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-449] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-449] for track '41' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [359-386] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-399] for track '43' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.