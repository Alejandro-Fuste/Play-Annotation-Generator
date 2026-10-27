# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_178`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_178/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 104 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '14' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [0-158] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-167] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-187] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-198] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-214] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-242] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-253] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-294] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-298] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-237] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-193] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-205] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-290] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-325] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-279] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-283] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-290] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-299] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [301-329] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [168-197] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [200-253] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [256-297] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '6' starts at frame 200, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [200-200] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-220] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-108] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-132] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-179] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-186] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-214] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-256] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-294] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [163-183] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [192-240] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-303] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-22] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-55] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-182] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-265] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-114] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-158] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-178] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-187] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-263] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-79] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-106] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-158] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [163-172] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [178-182] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-207] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-191] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-208] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-329] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [210-288] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [218-248] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-271] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-275] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-329] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-275] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-329] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-276] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-281] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-285] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-324] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-295] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-329] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-314] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-329] for track '32' has 1 frames without a visible bounding box.
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