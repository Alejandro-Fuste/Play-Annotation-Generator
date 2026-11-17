# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_371`
- **Input XML**: `outputs/batch/Power/Power/Power_371/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 113 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-101] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-226] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-230] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-168] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-175] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-118] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-168] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-217] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-126] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-141] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-145] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [79-83] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [92-102] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [115-118] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [125-126] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-173] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-224] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-100] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-134] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-147] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-6] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-22] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-28] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-86] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-104] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-108] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-116] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-126] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-93] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-98] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-110] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-79] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-86] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-81] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-159] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-168] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-177] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-192] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-28] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [79-101] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [105-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [115-122] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [125-126] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [131-141] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-168] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-83] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-83] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-86] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-97] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-108] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-118] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [79-86] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [88-108] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [115-127] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-86] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-98] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-124] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-110] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-132] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-162] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-187] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-206] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-214] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-224] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-236] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-201] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-226] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-232] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-236] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-168] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-179] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-189] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-222] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-228] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-193] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-186] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-215] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-222] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-239] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-228] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-239] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-208] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-239] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-232] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-239] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-239] for track '38' has 1 frames without a visible bounding box.
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
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.