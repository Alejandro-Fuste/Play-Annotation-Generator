# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_224`
- **Input XML**: `outputs/batch/Power/Power/Power_224/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 450: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [4-159] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-128] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-189] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-234] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-191] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-205] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-114] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-126] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-158] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-167] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-173] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-284] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [126-154] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [158-165] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-200] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-241] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-257] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-264] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-275] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-162] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-171] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-263] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-292] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-146] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-178] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-193] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-153] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-28] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-33] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-66] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-123] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-136] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-196] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-272] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-224] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-123] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [130-131] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-8] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-64] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-86] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-173] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-23] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-30] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-43] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-64] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-127] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-164] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-182] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-195] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-34] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-129] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-168] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [126-131] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [136-145] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 178, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [178-178] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-154] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-201] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-229] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-222] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-226] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-268] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-299] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-294] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-275] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-219] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-227] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-234] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-252] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-256] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-271] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-264] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-277] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-295] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-276] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-285] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-287] for track '29' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.