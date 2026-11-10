# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_74`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_74/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Action 'Action_None' range [81-142] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-130] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-104] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-375] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-145] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-134] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-123] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-131] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-163] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PullBall' range [88-96] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-154] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-115] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-112] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-98] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-130] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-96] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-173] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 81, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [81-142] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-85] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [87-96] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-99] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '17' starts at frame 122, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [122-124] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-130] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-61] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-71] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-161] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-137] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-157] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-139] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-215] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-219] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-223] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-243] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-469] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-371] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-400] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-384] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-453] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-461] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [465-471] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-479] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-421] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-362] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [366-367] for track '33' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.