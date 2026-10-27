# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Dagger_24`
- **Input XML**: `outputs/batch/Dagger/Dagger/Dagger_24/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Dagger.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 26: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [130–134], lower_priority='Action_PassBlock' annotated_start=133, effective_Action_PassBlock_start=135.
> - Action 'Action_None' range [270-285] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-298] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-247] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-148] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-308] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-247] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-155] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-165] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-185] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-212] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-222] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-144] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-171] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [135-144] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-306] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-317] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-144] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-145] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-145] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [133-142] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [173-319] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [322-324] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [328-329] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-145] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-154] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [221-223] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [225-226] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-246] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [133-144] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [133-144] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-145] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-153] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-247] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-203] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-213] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-274] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-215] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-223] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-235] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-252] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-274] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-329] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '30' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.