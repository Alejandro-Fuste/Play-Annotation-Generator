# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_114`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_114/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 138 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Segment 'Action_BallCarry' for track '10' has invalid range: start=140, end=125. Clamping end to start.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [99–110], lower_priority='Action_DownBlock' annotated_start=100, effective_Action_DownBlock_start=111.
> - Action 'Action_PreSnap' range [0-66] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-329] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [99-178] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-218] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-244] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-308] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-317] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-114] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-138] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-167] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-194] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-270] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [273-296] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [100-151] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-181] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-218] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-247] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-274] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-211] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-329] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-171] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-115] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [122-125] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [128-139] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '9' starts at frame 140, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [140-140] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [100-111] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [140-142] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [99-110] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [111-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-183] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-199] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-51] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-65] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-76] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [100-104] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [131-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-185] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [100-136] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [147-173] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-186] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-272] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-133] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-204] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [206-276] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-98] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-128] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-96] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-102] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-116] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-183] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-193] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-163] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-217] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-227] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-129] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-157] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-247] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-296] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-327] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-145] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-217] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-329] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [154-159] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-250] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-329] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-171] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-265] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [172-203] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-250] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-290] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-188] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-211] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-244] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-194] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-217] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-203] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-269] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-217] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-258] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-294] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-329] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-259] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-299] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-242] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-249] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-267] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-277] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-283] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-293] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-302] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-255] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-306] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [308-329] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-289] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-307] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-318] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-329] for track '40' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.