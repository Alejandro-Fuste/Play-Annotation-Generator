# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_216`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_216/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 43 |
| Player Tracks | 43 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 130 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [74–89], lower_priority='Action_DownBlock' annotated_start=75, effective_Action_DownBlock_start=90.
> - Action 'Action_None' range [74-253] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-95] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-146] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-178] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-161] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-178] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [74-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-177] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-171] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [75-135] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-84] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [75-106] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-189] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-201] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-232] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [75-88] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [92-107] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-153] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-93] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [102-107] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [134-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-132] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-162] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-183] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-211] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-30] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-43] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-87] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-124] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [90-108] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [110-129] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [145-149] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-127] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-209] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-17] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-33] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-94] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-21] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-67] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [75-90] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [118-119] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-67] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-126] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-169] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-212] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-132] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [138-190] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-198] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-113] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-122] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-125] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-145] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-151] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-128] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-183] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-217] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-229] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-238] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-133] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-165] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-179] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-220] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-252] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-179] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-205] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-214] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-182] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-199] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-216] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-241] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-250] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-268] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-173] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-262] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-211] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-217] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [197-217] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-229] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-209] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-232] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-242] for track '42' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.