# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_266`
- **Input XML**: `outputs/batch/Power/Power/Power_266/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 532: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [28-121] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-176] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-186] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-168] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-232] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-133] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-136] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [115-140] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-189] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-219] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-237] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-107] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-111] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-131] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-187] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-239] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-118] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-125] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-151] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-155] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-203] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-161] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-239] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-131] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-192] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-236] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [115-116] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [128-166] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-109] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-213] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-218] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-223] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-163] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-189] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-197] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-213] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-45] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-106] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-114] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-86] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-89] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [115-126] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-162] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-151] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-134] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-165] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-190] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-218] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-160] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-172] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-215] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-196] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-189] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-195] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-203] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-217] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-201] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-234] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-211] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-239] for track '27' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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