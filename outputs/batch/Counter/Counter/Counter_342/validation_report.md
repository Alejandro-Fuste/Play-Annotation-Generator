# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_342`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_342/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 120 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 686: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [104–117], lower_priority='Action_DownBlock' annotated_start=107, effective_Action_DownBlock_start=118.
> - Action 'Action_None' range [104-237] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-111] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-157] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-295] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [104-197] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-250] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [257-289] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [104-242] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [271-280] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [107-122] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-182] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-213] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [107-117] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-154] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-299] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [118-141] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-122] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-138] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-151] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-97] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-101] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-121] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-149] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-214] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [107-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [129-138] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [107-111] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [113-118] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [123-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [150-151] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [153-155] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [158-184] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-140] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [141-159] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [167-229] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [235-260] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [263-299] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-26] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-35] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-115] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-22] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-31] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-196] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-130] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-141] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-213] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-299] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-195] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-206] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-214] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-237] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-170] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-265] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-224] for track '24' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-187] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-257] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-299] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-208] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-204] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-233] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-229] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-233] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-270] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-298] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-242] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '31' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.