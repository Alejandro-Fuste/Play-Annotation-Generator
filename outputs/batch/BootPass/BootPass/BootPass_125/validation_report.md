# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_125`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_125/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_SecureCatch' for track '4' has invalid range: start=308, end=299. Clamping end to start.
> - Segment 'Action_BallSnap' for track '8' has invalid range: start=72, end=64. Clamping end to start.
> - Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [72–72], lower_priority='Action_RunBlock' annotated_start=64, effective_Action_RunBlock_start=73.
> - Segment 'Action_SnapReceive' for track '16' has invalid range: start=72, end=64. Clamping end to start.
> - Action 'Action_PreSnap' range [0-277] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-109] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-278] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-288] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-217] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-178] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-192] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-237] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [64-101] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-294] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BootAway' range [98-129] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [64-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-95] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-108] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-117] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-294] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-276] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [64-123] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-175] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-160] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-299] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-266] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-281] for track '28' has 1 frames without a visible bounding box.
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
> - Action event 'Action_SecureCatch' has invalid start frame 308. Video range is [0, 299].

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.