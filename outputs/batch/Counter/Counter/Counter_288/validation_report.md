# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_288`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_288/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '2' (C) duration 91 frames exceeds threshold 90 frames [start=110, end=200].
> - Resolved action overlap for track '2' (C): higher_priority='Action_BallSnap' [107–121], lower_priority='Action_DownBlock' annotated_start=110, effective_Action_DownBlock_start=122.
> - Validation warning: Action 'Action_DownBlock' for track '9' (LT) duration 91 frames exceeds threshold 90 frames [start=110, end=200].
> - Validation warning: Action 'Action_DownBlock' for track '12' (LG) duration 91 frames exceeds threshold 90 frames [start=110, end=200].
> - Validation warning: Action 'Action_PullBlock' for track '14' (RG) duration 91 frames exceeds threshold 90 frames [start=110, end=200].
> - Action 'Action_None' range [107-128] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-329] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [122-145] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-255] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-143] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-222] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-228] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-257] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-158] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [110-200] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-280] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-311] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-325] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-225] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-240] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [110-200] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-211] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-176] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-260] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-181] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-266] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-77] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-157] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-162] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-186] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-236] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-185] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-294] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-329] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-189] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-203] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-214] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [216-222] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-230] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-292] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-327] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-307] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-269] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-294] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-303] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-319] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-313] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.