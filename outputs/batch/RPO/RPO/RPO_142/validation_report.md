# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_142`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_142/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 52 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['C', 'LG', 'LT', 'RT'].

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-233] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-256] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-196] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-159] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-183] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-115] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-156] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-174] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-177] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-182] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-192] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-108] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-116] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-96] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-183] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-153] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-248] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-254] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-261] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-84] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-151] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-257] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-118] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-213] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-256] for track '24' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.