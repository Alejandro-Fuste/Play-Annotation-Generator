# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_39`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_39/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 55 |
| Player Tracks | 55 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 134 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [12–28], lower_priority='Action_PassBlock' annotated_start=15, effective_Action_PassBlock_start=29.
> - Action 'Action_None' range [12-176] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_SellOut' range [79-80] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [94-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [122-125] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-125] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-58] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-127] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-184] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-194] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-92] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-226] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-179] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-203] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-224] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-55] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [58-84] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [86-128] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [29-56] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [58-74] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [82-87] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [89-127] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-75] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-80] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-221] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-232] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-117] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-153] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-167] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-186] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-216] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [12-127] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-221] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-130] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-93] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-98] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-82] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-127] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-175] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-129] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-161] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-175] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-123] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-127] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-155] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-175] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-176] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-203] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-168] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-188] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-202] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-217] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-181] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-239] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-181] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-196] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-239] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-239] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-189] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-200] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-209] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-200] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-239] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-239] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-218] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-227] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-222] for track '49' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [213-227] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-232] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-232] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-232] for track '53' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.