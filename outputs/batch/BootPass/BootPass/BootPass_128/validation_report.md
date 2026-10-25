# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_128`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_128/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Segment 'Action_BallSnap' for track '4' has invalid range: start=110, end=23. Clamping end to start.
> - Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [110–110], lower_priority='Action_RunBlock' annotated_start=23, effective_Action_RunBlock_start=111.
> - Overlapping action conflict at frame 23 for track '12': 'Action_RunBlock' vs 'Action_SnapReceive'. Overriding with 'Action_SnapReceive'.
> - Segment 'Action_SnapReceive' for track '12' has invalid range: start=110, end=23. Clamping end to start.
> - Segment 'Action_SecureCatch' for track '29' has invalid range: start=264, end=194. Clamping end to start.
> - Segment 'Action_ThrowPass' for track '33' has invalid range: start=311, end=154. Clamping end to start.
> - Action 'Action_None' range [110-227] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [23-168] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [174-177] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-143] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-157] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-163] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-140] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-229] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-172] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-223] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-239] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-256] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-300] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-129] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-153] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [23-125] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [155-206] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [208-236] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [284-294] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-138] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-158] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-142] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-147] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-189] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-230] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-121] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-186] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-227] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [23-163] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [170-231] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-144] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-139] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-124] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-141] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-199] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-154] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-189] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-227] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-231] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-175] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-228] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-175] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-198] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-217] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-183] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-225] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-223] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-218] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-250] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-245] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-248] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-311] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-322] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-284] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-323] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-315] for track '33' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.