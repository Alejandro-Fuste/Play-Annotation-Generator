# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_145`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_145/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 133 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 292: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_None' range [150-177] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-184] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-208] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-220] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-159] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-169] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-278] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-304] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-325] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-280] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [188-213] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [220-236] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [238-311] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-176] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-183] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-148] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-156] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-195] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-313] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-160] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-200] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-211] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [177-187] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-233] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-304] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-310] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-329] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-160] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-181] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-260] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-312] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-320] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-280] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-299] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-245] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-266] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-274] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-199] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-236] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-277] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-281] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-303] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-326] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-230] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-270] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [152-228] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '16' starts at frame 234, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [234-236] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-259] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-314] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [152-171] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-206] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-158] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [152-160] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [167-168] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [171-172] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [174-198] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [201-233] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-250] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-264] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-162] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-204] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-329] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-256] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-302] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-311] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-281] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-285] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-296] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [305-310] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-311] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-262] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-317] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [256-311] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-329] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-312] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-320] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-310] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-329] for track '29' has 1 frames without a visible bounding box.
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