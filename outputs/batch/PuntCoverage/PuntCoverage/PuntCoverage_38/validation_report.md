# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_38`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_38/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-234] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-183] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-234] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-250] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-195] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-68] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-208] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-221] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-163] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-255] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-52] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-90] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-182] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [184-199] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [201-227] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_Tackle' range [231-235] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [52-61] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-48] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-263] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [198-217] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-243] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-161] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-121] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-110] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-128] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-133] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-165] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-163] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-193] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-236] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-267] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-243] for track '35' has 1 frames without a visible bounding box.
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
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.