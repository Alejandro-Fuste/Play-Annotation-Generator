# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_123`
- **Input XML**: `outputs/batch/Power/Power/Power_123/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 105 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Overlapping action conflict at frame 108 for track '18': 'Action_DownBlock' vs 'Action_PullBlock'. Overriding with 'Action_PullBlock'.
> - Action 'Action_PreSnap' range [9-147] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-155] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-172] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-179] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-233] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-250] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-264] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-187] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-177] for track '6' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-189] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-221] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-147] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-230] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-101] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-114] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-144] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-116] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-100] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-113] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-101] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-112] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-251] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-257] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [110-112] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-100] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [110-112] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [133-145] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [150-155] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [158-163] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-181] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-244] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-249] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-107] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [108-114] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [116-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [124-126] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [133-135] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [138-147] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [149-156] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [158-159] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-99] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-114] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-135] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-147] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-230] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-241] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-248] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-147] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-151] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-114] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-147] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-229] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-269] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-144] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-156] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-169] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-135] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-145] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-147] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-151] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-170] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-174] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-242] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-258] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-189] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-196] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-227] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-236] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-251] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-196] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-239] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-248] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-251] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-255] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-269] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-251] for track '30' has 1 frames without a visible bounding box.
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