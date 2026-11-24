# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_341`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_341/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 122 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [102–114], lower_priority='Action_DownBlock' annotated_start=105, effective_Action_DownBlock_start=115.
> - Action 'Action_None' range [102-214] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-290] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [144-207] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [105-178] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [180-191] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-195] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-267] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [270-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-155] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [102-213] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-194] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-171] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-222] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [105-141] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [143-160] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-197] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-214] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-299] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-283] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-292] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [105-149] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [155-159] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-126] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-181] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-190] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-202] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-214] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-197] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [105-140] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-194] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-208] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-233] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-245] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-165] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-176] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-209] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-223] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-233] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-129] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-155] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-172] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-252] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-262] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-151] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-174] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-207] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-189] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-229] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-269] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-203] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-212] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-299] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-207] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-216] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-299] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-238] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-243] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-255] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-261] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-299] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-286] for track '39' has 1 frames without a visible bounding box.
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