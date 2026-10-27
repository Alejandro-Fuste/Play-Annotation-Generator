# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_51`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_51/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 101 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 104: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '17' (C) duration 92 frames exceeds threshold 90 frames [start=107, end=198].
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [99–112], lower_priority='Action_DownBlock' annotated_start=107, effective_Action_DownBlock_start=113.
> - Validation warning: Action 'Action_DownBlock' for track '19' (LG) duration 92 frames exceeds threshold 90 frames [start=107, end=198].
> - Action 'Action_None' range [99-216] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-299] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-237] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-247] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-253] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-275] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-161] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-174] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-194] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-203] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-253] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-266] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-284] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-291] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-151] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-170] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-297] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-158] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-214] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-248] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-286] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-288] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-162] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [107-154] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-134] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-172] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-216] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [99-112] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [115-117] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [119-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [123-129] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-286] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-185] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [107-113] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [115-136] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [138-156] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [192-193] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-246] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-252] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [107-154] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [156-162] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-111] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-122] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-160] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-203] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-242] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-171] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-204] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-195] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [197-242] for track '24' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [245-280] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-208] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-246] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-299] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [292-295] for track '29' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.