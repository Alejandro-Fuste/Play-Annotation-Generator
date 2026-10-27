# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `CrackToss_48`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_48/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_None' at frame 117 targets track ID '154', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '5' (RT) duration 128 frames exceeds threshold 90 frames [start=73, end=200].
> - Action 'Action_None' range [70-200] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [70-133] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-200] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [73-99] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-175] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [104-166] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [169-173] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [175-195] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [73-142] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [144-200] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [70-145] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-200] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-92] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-178] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-195] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [73-98] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [100-105] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [112-200] for track '10' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [70-86] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-116] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-200] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-191] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [195-200] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [70-162] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [165-177] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-186] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-190] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-117] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-142] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-98] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-147] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-176] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-200] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-194] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-147] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-190] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-200] for track '24' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.