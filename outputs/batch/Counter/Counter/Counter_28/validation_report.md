# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_28`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_28/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 39 |
| Ball Tracks | 1 |
| CSV events parsed | 18 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [120–135], lower_priority='Action_DownBlock' annotated_start=127, effective_Action_DownBlock_start=136.
> - Action 'Action_BallCarry' range [179-191] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [201-287] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-171] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-168] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '3' starts at frame 208, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [208-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-203] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-299] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [120-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-165] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-171] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-198] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-157] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-171] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [127-147] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [127-144] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-141] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [136-137] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [145-149] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [151-194] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [196-207] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-130] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-137] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-166] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-192] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-122] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-135] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-142] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-151] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-177] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-153] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-256] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-175] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-205] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-179] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-207] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-216] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-223] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-240] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-255] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-285] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-276] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-286] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-272] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-282] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-299] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-293] for track '39' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.