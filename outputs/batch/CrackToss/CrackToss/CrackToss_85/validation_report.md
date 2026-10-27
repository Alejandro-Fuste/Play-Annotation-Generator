# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_85`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_85/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 37 |
| Ball Tracks | 1 |
| CSV events parsed | 16 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 349 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 349 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [242–253], lower_priority='Action_PullBlock' annotated_start=245, effective_Action_PullBlock_start=254.
> - Segment 'Action_BallCarry' for track '25' has invalid range: start=276, end=34. Clamping end to start.
> - Action 'Action_PreSnap' range [0-7] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-333] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-253] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-273] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-291] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [245-260] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-339] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [254-280] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [285-288] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [291-311] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-263] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-304] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-318] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-273] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-349] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-259] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-307] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [309-311] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-349] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-34] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-241] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-258] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [245-308] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [310-324] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-325] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-335] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-285] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-292] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-345] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-294] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-337] for track '36' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.