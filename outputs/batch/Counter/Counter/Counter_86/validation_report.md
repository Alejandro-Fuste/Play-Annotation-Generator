# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_86`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_86/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 174: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_BallCarry' for track '1' has invalid range: start=178, end=168. Clamping end to start.
> - Overlapping action conflict at frame 140 for track '4': 'Action_DownBlock' vs 'Action_PullBlock'. Overriding with 'Action_PullBlock'.
> - Action 'Action_PreSnap' range [0-168] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-240] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-198] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-223] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-299] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [140-165] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-220] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-244] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-160] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-176] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-186] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [140-171] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-247] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-233] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [138-153] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [140-168] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [174-182] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [187-199] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-159] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-182] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-186] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-167] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-206] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-216] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-289] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-235] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-287] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-201] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-299] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [194-197] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-285] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-299] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-247] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-276] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-284] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-276] for track '27' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.