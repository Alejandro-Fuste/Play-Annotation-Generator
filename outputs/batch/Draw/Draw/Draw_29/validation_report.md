# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_29`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_29/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 117 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [75–87], lower_priority='Action_PassBlock' annotated_start=78, effective_Action_PassBlock_start=88.
> - Action 'Action_None' range [75-177] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-284] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [292-297] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-312] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-310] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-148] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-152] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-258] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-283] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-295] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-303] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-192] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-224] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [229-257] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-263] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-182] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-144] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-153] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-176] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-309] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [182-257] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-262] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-230] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-100] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-293] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-303] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-312] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [316-324] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-206] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [127-144] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [78-141] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [148-181] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-262] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-273] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-329] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-117] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [78-126] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [132-181] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-329] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' for track '21' starts at frame 88, but the player has no visible bounding box on this frame.
> - Action 'Action_PassBlock' range [88-98] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [100-101] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [103-108] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [110-181] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-235] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-283] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [305-311] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-322] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-248] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-279] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-263] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-181] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-196] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-329] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [187-246] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-251] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-272] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-279] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-308] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [323-325] for track '33' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.