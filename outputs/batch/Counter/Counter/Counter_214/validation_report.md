# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_214`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_214/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 43 |
| Player Tracks | 42 |
| Ball Tracks | 1 |
| CSV events parsed | 20 |
| Action Segments inferred | 130 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '8' (LT) duration 139 frames exceeds threshold 90 frames [start=99, end=237].
> - Validation warning: Action 'Action_DownBlock' for track '9' (LG) duration 139 frames exceeds threshold 90 frames [start=99, end=237].
> - Validation warning: Action 'Action_DownBlock' for track '11' (C) duration 139 frames exceeds threshold 90 frames [start=99, end=237].
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [97–99], lower_priority='Action_DownBlock' annotated_start=99, effective_Action_DownBlock_start=100.
> - Validation warning: Action 'Action_PullBlock' for track '12' (RG) duration 139 frames exceeds threshold 90 frames [start=99, end=237].
> - Action 'Action_None' range [97-233] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [259-261] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-283] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-147] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-226] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-122] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-128] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-139] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-124] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-169] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-171] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-389] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-147] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-155] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-169] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-188] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [138-147] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [149-389] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-143] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-221] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-374] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [99-181] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [183-230] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [232-237] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [99-237] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [99-169] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [172-173] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [175-177] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [179-236] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [99-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [128-155] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-355] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-140] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-211] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-200] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-234] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-251] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-270] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-29] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-96] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-127] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-197] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-136] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-178] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-200] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-274] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [283-289] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-200] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-249] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-262] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [265-283] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-290] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-349] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-388] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-200] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-389] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-220] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-380] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-389] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-240] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-243] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-321] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-342] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-389] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-283] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-312] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-317] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-319] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-332] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-340] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-359] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-332] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [338-340] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-349] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-359] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-377] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [379-383] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-337] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-344] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-343] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-345] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-352] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-357] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-389] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-383] for track '42' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.