# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_40`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_40/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 29 |
| Ball Tracks | 1 |
| CSV events parsed | 19 |
| Action Segments inferred | 108 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [70–84], lower_priority='Action_PassBlock' annotated_start=73, effective_Action_PassBlock_start=85.
> - Segment 'Action_Handoff' for track '10' has invalid range: start=101, end=97. Clamping end to start.
> - Action 'Action_PassBlock' range [73-119] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [70-237] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-144] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-152] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-152] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [154-158] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-163] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-224] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-240] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-244] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-299] for track '3' has 7 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [85-86] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [88-103] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [105-127] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [131-158] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-201] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-296] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-299] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-131] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-185] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [187-225] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-250] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [252-268] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-285] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-299] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-152] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-103] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [111-112] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [115-118] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [123-129] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [133-149] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-96] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-103] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-126] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-152] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-166] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-195] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-295] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_FakePassDroptoHandoff' range [86-97] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-92] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-94] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-89] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-100] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-112] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [113-121] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [123-152] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [154-278] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-175] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-127] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-152] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-177] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-185] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-231] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-291] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-299] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-240] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-299] for track '19' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-201] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-231] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-248] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-258] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-283] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [294-299] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-258] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-298] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-248] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-291] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-285] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [291-293] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-277] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-296] for track '27' has 2 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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