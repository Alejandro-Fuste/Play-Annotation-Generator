# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_193`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_193/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [82-134] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-175] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-244] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-266] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-141] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-158] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-236] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [241-279] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-223] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-121] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [122-235] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [246-256] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [261-289] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-243] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-152] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-104] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-142] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-152] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-173] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-233] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-219] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-237] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-282] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-184] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-276] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [89-122] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-248] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-125] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-130] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-228] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [89-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-179] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-242] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-191] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-205] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-215] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-236] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-247] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-256] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-270] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-286] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-297] for track '28' has 2 frames without a visible bounding box.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.