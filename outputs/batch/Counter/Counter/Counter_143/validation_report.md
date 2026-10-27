# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_143`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_143/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [161–175], lower_priority='Action_DownBlock' annotated_start=164, effective_Action_DownBlock_start=176.
> - Action 'Action_None' range [161-235] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-306] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-327] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [164-229] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [232-234] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-329] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [164-246] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-329] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-251] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-274] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-246] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-273] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-311] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [316-318] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-322] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-281] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-300] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-279] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [164-189] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [203-204] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-311] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [313-315] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-327] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-227] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-233] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-257] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-194] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-211] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-329] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [197-236] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [239-307] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [314-319] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-226] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [176-189] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [164-179] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [189-201] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [204-205] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [209-214] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [225-227] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [236-237] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-225] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-253] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-329] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-254] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-254] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-329] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-280] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [282-287] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-301] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-286] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [284-286] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-292] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-300] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.